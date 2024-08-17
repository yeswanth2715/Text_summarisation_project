from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger
import time

def log_stage_duration(stage_name, func):
      """Log duration of a pipeline stage."""
      start_time= time.time()
      try:
            logger.info(f">>>> {stage_name} started <<<<")
            func()
            end_time= time.time()
            duration= end_time - start_time
            logger.info(f"{stage_name} completed in {duration:.2f} seconds.")
      except Exception as e:
            logger.error(f"{stage_name} failed with error: {str(e)}")
            raise e

#Data Ingestion Stage
log_stage_duration("Data Ingestion Stage", lambda: DataIngestionTrainingPipeline().main())

#Data Validation Stage
log_stage_duration("Data Validation Stage", lambda: DataValidationTrainingPipeline().main())

#Data Transformation Stage
log_stage_duration("Data Transformation Stage", lambda: DataTransformationTrainingPipeline().main())

#Model Training Stage
log_stage_duration("Model Training Stage", lambda: ModelTrainerTrainingPipeline().main())

#Model Evaluation Stage
log_stage_duration("Model Evaluation Stage", lambda: ModelEvaluationTrainingPipeline().main())





